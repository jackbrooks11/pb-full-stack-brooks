export class WhaleSighting {
    constructor(
        public id: number,
        public spotter_project_id: number,
        public spotter_trip_id: number,
        public evt_date: string,
        public evt_datetime_utc: Date,
        public vessel: string,
        public lat_d: number,
        public long_d: number,
        public commonname: string,
        public observationcount: number,
        public behavior: string,
        public distance: number,
        public reticle: number,
        public bearing: number,
        public comments: string,
        public corrected_latitude: number,
        public corrected_longitude: number
    ) { }
  }