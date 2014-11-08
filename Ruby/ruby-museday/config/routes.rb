RubyMuseday::Application.routes.draw do
  resources :submissions do
     resources :submitted_poems
  end
  resources :poems
  resources :submitted_poem_statuses
  resources :publications

  get "welcome/index"
end
