import { Component , OnInit} from '@angular/core';
import {UserService} from './user.service';
import {ApplicationService} from './application.service';
import { from, throwError } from 'rxjs';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'frontend';

  public users;

  public applications;

  public new_application: any;

  constructor(private _applicationService: ApplicationService, private _userService:UserService)
  {  }

  ngOnInit()
  {
    this.getApplications();
    this.new_application ={};

    this.getUsers();
    // this.user ={
    //   name:'',
    //   password:''
    // };
  }

  getApplications(){
    this._applicationService.list().subscribe(

      data =>{
        this.applications = data;
      },

      err => console.error(err),
      () => console.log('done loading posts')
    );
  }

  getUsers(){
    this._userService.loadUsers().subscribe(

      data =>{
        this.users= data;
      },

      err => console.error(err),
      () => console.log('done loading users')
    );
  }

  createApplication(){
    this._applicationService.create(this.new_application).subscribe(
      data => {
        this.getApplications();
        return true;
      },
      error => {
        console.error("Error saving!");
        return throwError(error);
      }
    );
  }

}
