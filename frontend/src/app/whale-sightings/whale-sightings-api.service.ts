import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { API_URL } from '../env';
import { Injectable } from '@angular/core';

@Injectable()
export class WhaleSightingsApiService {
  constructor(private http: HttpClient) {}

  getWhaleSightings(year: number, species: string): Observable<any> {
    return this.http.get(`${API_URL}/get_sighting_data?year=${year}&species=${encodeURIComponent(species)}`);
  }
}