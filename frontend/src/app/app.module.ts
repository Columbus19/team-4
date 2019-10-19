import { BrowserModule } from '@angular/platform-browser';
import { NgModule, OnInit } from '@angular/core';
import {HttpClientModule} from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import {UserService} from './user.service';
import {FormsModule} from '@angular/forms';

@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    FormsModule,
    HttpClientModule,
    BrowserModule,
    AppRoutingModule
  ],
  providers: [UserService],
  bootstrap: [AppComponent]
})

export class AppModule implements OnInit 
{


  public user: any;

  constructor(private _userService: UserService){  }

  ngOnInit()
  {
    // this.user = {
    //   username: 'admin',
    //   password: '1234'
    // };
  }

  // login()
  // {
  //   this._userService.login({'username':this.user.username, 'password':this.user.password});
  // }

  // refreshToken(){
  //   this._userService.refreshToken();
  // }

  // logout(){
  //   this._userService.logout();
  // }

  loadApplications(){
    this._userService.loadUsers();
  }

}
