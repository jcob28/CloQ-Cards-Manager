Rails.application.routes.draw do
  root to: proc { [404, {}, ["404 \n Go to http://127.0.0.1:3000/api"]] }

  get '/api' => redirect('/swagger/dist/index.html?url=/api-docs.json')

  namespace 'v1' do
    root to: proc { [404, {}, ["404 \n Go to http://127.0.0.1:3000/api"]] }

    post '/login', to: 'sessions#login'

    resources :registers
    resources :vacations
    resources :employees
    resources :gates
    resources :positions
    resources :managers
    resources :users

    end
end
