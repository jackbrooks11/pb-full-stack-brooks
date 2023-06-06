import { Component, OnDestroy, OnInit } from '@angular/core';
import { WhaleSightingsApiService } from './whale-sightings/whale-sightings-api.service';
import { ChartDataset, ChartOptions } from 'chart.js';
import { WhaleSighting } from './whale-sightings/whale-sighting.model';
import { Subscription } from 'rxjs';
@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  // Initialize selectedYear and selectedSpecies
  selectedYear: number | null = null;
  selectedSpecies: string | null = null;
  years: number[] = [];
  species: string[] = [];

  chartData: ChartDataset[] = [];
  chartLabels: any[] = [];
  chartOptions: ChartOptions = {
    responsive: true,
    maintainAspectRatio: false,
    scales: {
      y: {
        beginAtZero: true,
        ticks: {
          stepSize: 1,
          precision: 0
        }
      }
    },
    // Other chart options...
    plugins: {
      title: {
        display: true,
        text: '',
        font: {
          size: 16
        }
      }
    }
  };
  chartLegend = true;
  showGraph = false;

  constructor(private whaleSightingsApi: WhaleSightingsApiService) {}

  ngOnInit() {
    this.fetchUniqueYears();
    this.fetchUniqueSpecies();
  }

  ngOnDestroy() {}

  onSelectionChange(): Subscription {
    if (this.selectedYear && this.selectedSpecies) {
      return this.whaleSightingsApi.getWhaleSightings(this.selectedYear, this.selectedSpecies)
        .subscribe({
          next: (res: WhaleSighting[]) => {
            this.showGraph = true;
            // Update the chart title
            if (this.chartOptions.plugins && this.chartOptions.plugins.title) {
              this.chartOptions.plugins.title.text = `Observation Count for ${this.selectedSpecies} (${this.selectedYear})`;
            }
            const sightings = res;
            const chart_data = new Array(12).fill(0); // Initialize an array of 12 months with observation count set to 0
            for (const sighting of sightings) {
              const month = parseInt(sighting.evt_date.substring(4, 6)); // Extract month from evt_date
              chart_data[month - 1] += 1;
            }
            const months = ['January', 'February', 'March', 'April', 'May', 'June',
              'July', 'August', 'September', 'October', 'November', 'December'];
            this.chartData = [{ data: chart_data, label: 'Observation Count' }];
            this.chartLabels = months;
          },
          error: (error) => {
            console.error('Error fetching whale sightings:', error);
          }
        });
    } else {
      this.showGraph = false;
      return new Subscription(); // Return an empty subscription if no selection is made
    }
  }

  fetchUniqueYears(): Subscription {
    return this.whaleSightingsApi.getUniqueYears().subscribe({
      next: (data: number[]) => {
        this.years = data;
      },
      error: (error) => {
        console.error('Error fetching unique years:', error);
      }
    });
  }
  
  fetchUniqueSpecies(): Subscription {
    return this.whaleSightingsApi.getUniqueCommonnames().subscribe({
      next: (data: string[]) => {
        this.species = data;
      },
      error: (error) => {
        console.error('Error fetching unique species:', error);
      }
    });
  }

}