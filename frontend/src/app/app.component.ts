import { Component, OnDestroy, OnInit } from '@angular/core';
import {WhaleSighting} from './whale_sightings/whale_sighting.model';
import { WhaleSightingsApiService } from './whale_sightings/whale_sightings-api.service';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent implements OnInit, OnDestroy {
  title = 'app';
  whaleSightingsList: any;

  constructor(private whaleSightingsApi: WhaleSightingsApiService) {
  }

  ngOnInit() {
    this.whaleSightingsApi
      .getWhaleSightings()
      .subscribe(res => {
          this.whaleSightingsList = res;
        }
      );
  }

  ngOnDestroy() {

  }
}