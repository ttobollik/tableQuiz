import { Component, OnInit } from '@angular/core';
import { ApiService } from './api.service';

@Component({
  selector: 'app-root',
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css'],
  providers: [ApiService]
})
export class AppComponent implements OnInit{
  users;

  constructor ( private apiService: ApiService ) {
  }

  ngOnInit() {
    this.getAllUsers();
  }

  getAllUsers() {
    this.apiService.getAllUsers().subscribe(
      data => {
        this.users = data;
        console.log(this.users);
      }, 
      error => {
        console.log(error);
      });
  }

}
