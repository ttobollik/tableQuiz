import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { QuestionComponent } from './question.component';

@NgModule({
  declarations: [
    QuestionComponent
  ],
  imports: [
    BrowserModule
  ],
  providers: [],
  bootstrap: [QuestionComponent]
})
export class QuestionsModule { }
