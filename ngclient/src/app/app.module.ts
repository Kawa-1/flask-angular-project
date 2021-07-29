import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule } from '@angular/router';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { HttpClientModule, HTTP_INTERCEPTORS } from "@angular/common/http";

import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatTableModule } from '@angular/material/table';
import { MatPaginatorModule } from '@angular/material/paginator';
import { MatSortModule } from '@angular/material/sort';
import { AppRoutingModule } from './app-routing.module';
import { RecaptchaModule } from "ng-recaptcha";
import { CookieService } from 'ngx-cookie-service';
import { ToastrModule } from 'ngx-toastr';
import { StoreModule } from '@ngrx/store';
import { StoreDevtoolsModule } from '@ngrx/store-devtools';
import { EffectsModule } from '@ngrx/effects';

import { AppComponent } from './app.component';
import { RestaurantsComponent } from './restaurants/restaurants.component';
import { AddRecipeComponent } from './add-recipe/add-recipe.component';
import { NavbarComponent } from './navbar/navbar.component';
import { HomeComponent } from './home/home.component';
import { YourProfileComponent } from './your-profile/your-profile.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component'
import { RecipesComponent } from './recipes/recipes.component';
import { NotFoundComponent } from './not-found/not-found.component';
import { RecaptchaComponent } from './recaptcha/recaptcha.component';
import { OpinionsComponent } from './opinions/opinions.component';

import { ChildComponent } from './child/child.component';
import { ButtonsComponent } from './buttons/buttons.component';

import { LoadMapService } from './services/load-map.service';
import { AuthService } from './services/auth.service';
import { AuthInterceptor } from './services/auth.interceptor';

@NgModule({
  declarations: [
    AppComponent,
    RestaurantsComponent,
    AddRecipeComponent,
    NavbarComponent,
    HomeComponent,
    YourProfileComponent,
    LoginComponent,
    RegisterComponent,
    RecipesComponent,
    NotFoundComponent,
    RecaptchaComponent,
    OpinionsComponent,
    ButtonsComponent,
    ChildComponent,
  ],
  imports: [
    FormsModule,
    HttpClientModule,
    ReactiveFormsModule,
    RecaptchaModule,
    BrowserModule,
    AppRoutingModule,

    StoreDevtoolsModule.instrument({
      maxAge: 25
    }),
    RouterModule.forRoot([
      {
        path: '', 
        component: HomeComponent
      },
      {
        path: 'recipes', 
        component: RecipesComponent
      },
      {
        path: 'add-recipe', 
        component: AddRecipeComponent
      },
      {
        path: 'restaurants', 
        component: RestaurantsComponent
      },
      {
        path: 'restaurants/opinions', 
        component: OpinionsComponent
      },
      {
        path: 'your-profile', 
        component: YourProfileComponent
      },
      {
        path: 'login', 
        component: LoginComponent
      },
      {
        path: 'register', 
        component: RegisterComponent
      },
      {
        path: '**', 
        component: NotFoundComponent
      }
    ],{ onSameUrlNavigation: 'reload' }),
    BrowserAnimationsModule,
    MatTableModule,
    MatPaginatorModule,
    MatSortModule,
    ToastrModule.forRoot({
      timeOut:2000,
      preventDuplicates: true
    })
  ],
  providers: [
    AuthService, 
    CookieService, 
    LoadMapService,
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
