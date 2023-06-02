import {HttpClient, HttpErrorResponse} from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError } from 'rxjs/operators';
import {API_URL} from '../env';
import {WhaleSighting} from './whale_sighting.model';
import { Injectable } from '@angular/core';

@Injectable()
export class WhaleSightingsApiService {

  constructor(private http: HttpClient) {
  }

  // GET list of public, future events
  getWhaleSightings() {
    return this.http.get(`${API_URL}/get_sighting_data`);
  }
}