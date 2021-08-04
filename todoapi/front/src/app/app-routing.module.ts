import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { MatTableModule } from '@angular/material/table';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { MatButtonModule } from '@angular/material/button';
import { MatFormFieldModule } from '@angular/material/form-field';
import { MatInputModule } from '@angular/material/input';
import { FormsModule } from '@angular/forms';
import { MatIconModule } from '@angular/material/icon';

const routes: Routes = [];

@NgModule({
  imports: [RouterModule.forRoot(routes), BrowserModule, HttpClientModule, FormsModule, MatTableModule, MatButtonModule, MatFormFieldModule, MatInputModule, MatIconModule],
  exports: [RouterModule, FormsModule, MatTableModule, MatButtonModule, MatFormFieldModule, MatInputModule, MatIconModule]
})
export class AppRoutingModule { }