import { Component, OnDestroy, OnInit } from '@angular/core';
import { WhaleSightingsApiService } from './whale-sightings/whale-sightings-api.service';
import { ChartDataset, ChartOptions } from 'chart.js';
import { WhaleSighting } from './whale-sightings/whale-sighting.model';

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
  chartData: ChartDataset[] = [];
  chartLabels: any[] = [];
  chartOptions: ChartOptions = {
    responsive: true,
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

  ngOnInit() {}

  ngOnDestroy() {}

  onSelectionChange() {
    if (this.selectedYear && this.selectedSpecies) {
      this.whaleSightingsApi.getWhaleSightings(this.selectedYear, this.selectedSpecies)
        .subscribe(res => {
          this.showGraph = true;
          // Update the chart title
          if (this.chartOptions.plugins && this.chartOptions.plugins.title) {
            this.chartOptions.plugins.title.text = `Observation Count for ${this.selectedSpecies} (${this.selectedYear})`;
          }          var sightings = res as WhaleSighting[];
          const chart_data = new Array(12).fill(0); // Initialize an array of 12 months with observation count set to 0
          for (const sighting of sightings) {
            var month = parseInt(sighting.evt_date.substring(4, 6));
            chart_data[month - 1] += 1;
          }
          const months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'];
          this.chartData = [{ data: chart_data, label: 'Observation Count' }];
          this.chartLabels = months;
        });
    } else {
      this.showGraph = false;
    }
  }
}