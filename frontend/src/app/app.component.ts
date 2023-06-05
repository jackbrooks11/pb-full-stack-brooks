import { Component, OnDestroy, OnInit } from '@angular/core';
import { WhaleSightingsApiService } from './whale-sightings/whale-sightings-api.service';
import { ChartDataset, ChartOptions } from 'chart.js';

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
          const data = res as any[];
          console.log(data);
          const observationCounts = data.map(item => item.observationcount);
          const months = ['January', 'February', 'March', 'April', 'May', 'June',
            'July', 'August', 'September', 'October', 'November', 'December'];
          this.chartData = [{ data: observationCounts, label: 'Observation Count' }];
          this.chartLabels = months;
        });
    } else {
      this.showGraph = false;
    }
  }
}