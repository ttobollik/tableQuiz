import { BrowserModule } from '@angular/platform-browser';
import { NgModule } from '@angular/core';
import { QuestionsComponent } from './questions.component';
import { MatTableModule } from '@angular/material/table';

@NgModule({
  exports: [QuestionsComponent],
  declarations: [
    QuestionsComponent
  ],
  imports: [
    BrowserModule,
    MatTableModule
  ],
  providers: [],
  bootstrap: [QuestionsComponent]
})
export class QuestionsModule { }
