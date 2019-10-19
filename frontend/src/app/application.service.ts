import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';

import {UserService} from './user.service';
import { create } from 'domain';

@Injectable()
export class ApplicationService {


    private httpOptions: any;
    public errors: any = [];
    
    create(application){
        let httpOptions ={
            headers: new HttpHeaders({
                'Content-Type':'application/json',
                
            })
        };

        return this.http.post('/applications', JSON.stringify(application), shttpOptions);
    }


constructor(private http: HttpClient, private _userService: UserService)
 {
    this.httpOptions = {
        headers: new HttpHeaders({'Content-Type': 'application/json'})
      };

  }

  list(){
      return this.http.get('/applications');
  }

}
