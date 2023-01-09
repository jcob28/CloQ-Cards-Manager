module V1
  class VacationsController < ApplicationController
    before_action :set_vacation, only: %i[ show edit update destroy ]
    before_action :authenticate_request, only: %i[ index show create update destroy ]

    swagger_controller :vacations, 'Vacations'

    # GET /vacations
    swagger_api :index do
      summary 'Returns all vacations\' details'
      param :header, :Authorization, :string, :required, "Token"
    end

    def index
      @vacations = Vacation.all
      render json: @vacations, status: :ok
    end

    # GET /vacations/1
    swagger_api :show do
      summary 'Returns a vacation\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def show
      render json: @vacation, status: :ok
    end

    # POST /vacations
    swagger_api :create do
      summary 'Creates a vacation'
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def create
      @vacation = Vacation.new(vacation_params)
      if @vacation.save
        render json: @vacation, status: :created
      else
        render json: @vacation.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /vacations/1
    swagger_api :update do
      summary 'Updates a vacation\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def update
      @vacation = Vacation.new(vacation_params)
      if @vacation.save
        render json: @vacation, status: :created
      else
        render json: @vacation.errors, status: :unprocessable_entity
      end
    end

    # DELETE /vacations/1
    swagger_api :destroy do
      summary 'Deletes a vacation'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def destroy
      @vacation.destroy
      render json: { "Status":"Deleted" }, status: :ok
    end

    private

      def set_vacation
        @vacation = Vacation.find(params[:id])
      end

      def vacation_params
        params.permit(:employee_id, :start_date, :end_date, :vacation_type, :decision)
      end
  end
end

