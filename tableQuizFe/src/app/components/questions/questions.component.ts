import { Component, OnInit } from '@angular/core';
import { ApiService } from '../../api.service';

@Component({
  selector: 'app-questions',
  templateUrl: './questions.component.html',
  styleUrls: ['./questions.component.css']
})
export class QuestionsComponent implements OnInit {

  questions; 
  constructor(private apiService: ApiService) { }


  ngOnInit(): void {
  }

  getAllQuestions() {
    this.apiService.getAllUsers().subscribe(
      data => {
        this.questions = data;
      },
      error => {
        console.log(error);
      });
  }

}
