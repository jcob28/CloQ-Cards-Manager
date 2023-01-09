module V1
  class ManagersController < ApplicationController
    before_action :set_manager, only: %i[ show edit update destroy ]
    before_action :authenticate_request, only: %i[ create update destroy ]

    swagger_controller :managers, 'Managers'

    # GET /managers
    swagger_api :index do
      summary 'Returns all managers\' details'
    end

    def index
      @managers = Manager.all
      render json: @managers, status: :ok
    end

    # GET /managers/1
    swagger_api :show do
      summary 'Returns the manager\'s details'
      param :path, :id, :integer, :required, "User ID"
    end
    def show
      render json: @manager, status: :ok
    end

    # POST /managers
    swagger_api :create do
      summary 'Creates a manager'
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end
    def create
      @manager = Manager.new(manager_params)

      if @manager.save
        render json: @manager, status: :created
      else
        render json: @manager.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /managers/1
    swagger_api :update do
      summary 'Updates the manager\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end
    def update
      if @manager.update(manager_params)
        render json: :show, status: :ok
      else
        render json: @manager.errors, status: :unprocessable_entity
      end
    end

    # DELETE /managers/1
    swagger_api :destroy do
      summary 'Deletes a manager'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def destroy
      @manager.destroy
      render json: {"Status":"Deleted"}, status: :ok
    end

    private

      def set_manager
        @manager = Manager.find(params[:id])
      end

      def manager_params
        params.permit(:user_id)
      end
  end
end

