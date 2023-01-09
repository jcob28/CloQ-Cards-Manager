module V1

  class PositionsController < ApplicationController
    before_action :set_position, only: %i[ show edit update destroy ]
    before_action :authenticate_request, only: %i[ create update destroy ]

    swagger_controller :positions, 'Positions'

    # GET /positions
    swagger_api :index do
      summary 'Returns all positions\' details'
    end

    def index
      @positions = Position.all
      render json: @positions, status: :ok
    end

    # GET /positions/1
    swagger_api :show do
      summary 'Returns a position\'s details'
      param :path, :id, :integer, :required, "User ID"
    end

    def show
      @position = Position.find(params[:id])
    end

    # POST /positions
    swagger_api :create do
      summary 'Creates a position'
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def create
      @position = Position.new(position_params)

      if @position.save
        render json: @position, status: :created
      else
        render json: @position.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /positions/1
    swagger_api :update do
      summary 'Updates a position\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def update
      if @position.update(position_params)
        render json: :show, status: :ok
      else
        render json: @position.errors, status: :unprocessable_entity
      end
    end

    # DELETE /users/1
    swagger_api :destroy do
      summary 'Deletes a position'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def destroy
      @position.destroy
      render json: { "Status":"Deleted" }, status: :ok
    end

    private

      def set_position
        @position = Position.find(params[:id])
      end

      def position_params
        params.permit(:position_name, :salary)
      end
  end
end

