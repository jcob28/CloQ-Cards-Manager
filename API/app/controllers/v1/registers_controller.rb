module V1
  class RegistersController < ApplicationController
    before_action :set_register, only: %i[ show edit update destroy ]
    before_action :authenticate_request, only: %i[ index show create update destroy ]

    swagger_controller :registers, 'Registers'

    # GET /registers
    swagger_api :index do
      summary 'Returns all registers\' details'
      param :header, :Authorization, :string, :required, "Token"
    end

    def index
      @registers = Register.all
      render json: @registers, status: :ok
    end

    # GET /registers/1
    swagger_api :show do
      summary 'Returns a register\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def show
      render json: @register, status: :ok
    end

    # POST /registers
    swagger_api :create do
      summary 'Creates a register'
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def create
      @register = Register.new(register_params)
      if @register.save
        render json: @register, status: :created
      else
        render json: @register.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /registers/1
    swagger_api :update do
      summary 'Updates a register\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def update
      if @register.update(register_params)
        render json: @register, status: :ok
      else
        render json: @register.errors, status: :unprocessable_entity
      end
    end

    # DELETE /registers/1
    swagger_api :destroy do
      summary 'Deletes a register'
      param :path, :id, :integer, :required, "User ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def destroy
      @register.destroy
      render json: { "Status":"Deleted" }, status: :ok
    end

    private

      def set_register
        @register = Register.find(params[:id])
      end

      def register_params
        params.permit(:employee_id, :gate, :date_in, :time_in, :date_out, :time_out)
      end
  end
end
