import { Injectable } from '@angular/core';
import {HttpClient, HttpHeaders} from '@angular/common/http';


@Injectable()
export class UserService {

// http options used for making API calls
private httpOptions: any;

// the username of the logged in user
public username: string;

// error messages received from the login attempt
public errors: any = [];

constructor(private http: HttpClient) {

    this.httpOptions ={
        headers: new HttpHeaders({'Content-Type':'application/json'})
    };

}


public newUser(user)
{
    this.http.post('users/', JSON.stringify(user), this.httpOptions).subscribe(
        data => {
            // this.updateData(data['token']);
        },
        err=> {
            // this.errors = err['error'];
        }
    );
}


public newApplication(application)
{
    this.http.post('applications/', JSON.stringify(application), this.httpOptions).subscribe(

        data => {
        },

        err => {
            this.errors = err['error'];
        }

    );

}


public loadUsers()
{
    return this.http.get('users/');
}

}
