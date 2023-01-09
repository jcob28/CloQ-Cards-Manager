module V1

  class SessionsController < ApplicationController

    swagger_controller :sessions, 'Session'

    # POST /login
    swagger_api :login do
      summary 'Returns a token to authorize various actions'
      param :body, :body , :string, :required, "Request body"
    end
    def login
      user = User.find_by_login(params[:login])
      if user && user.authenticate(params[:password])
        token = jwt_encode(user_id: user.id)
        render json: { "token": token }, status: :ok
      else
        render json: { "error": "Incorrect login or password" }, status: :unauthorized
      end
    end
  end
end
