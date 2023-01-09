module V1
  class UsersController < ApplicationController
    before_action :authenticate_request, only: %i[ index show update destroy ]

    swagger_controller :users, 'Users'

    # GET /users
    swagger_api :index do
      summary 'Returns all users\' details'
    end

    def index
      @users = User.all
      render json: @users, status: :ok
    end

    # GET /users/1
    swagger_api :show do
      summary 'Returns an user\'s details'
      param :path, :id, :integer, :required, "User ID"
    end

    def show
      render json: @user, status: :ok
    end

    # POST /users
    swagger_api :create do
      summary 'Creates an user'
      param :body, :body, :string, :required, "Request body"
    end

    def create
      @user = User.new(user_params)

      if @user.save
        render json: @user, status: :created
      else
        render json: @user.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /users/1
    swagger_api :update do
      summary 'Updates an user\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def update
      if @user.update(user_params)
        render json: @user, status: :ok
      else
        render json: @user.errors, status: :unprocessable_entity
      end
    end

    # DELETE /users/1
    swagger_api :destroy do
      summary 'Deletes an user'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def destroy
      @user.destroy
      render json: { "Status":"Deleted" }, status: :ok
    end

    private

    def user_params
      params.permit(:login, :first_name, :last_name, :account_type, :email, :account_no, :password, :password_confirmation)
    end

    def update_params
      params.permit(:password, :password_confirmation, :nickname, :bio, :preferred_style)
    end
  end
end

