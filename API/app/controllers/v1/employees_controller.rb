module V1
  class EmployeesController < ApplicationController
    before_action :set_employee, only: %i[ show update destroy ]
    before_action :authenticate_request, only: [ :create, :update, :destroy ]

    swagger_controller :employees, 'Employees'

    # GET /employees
    swagger_api :index do
      summary 'Returns all employees\' details'
    end
    def index
      @employees = Employee.all
      render json: @employees, status: :ok
    end

    # GET /employees/1
    swagger_api :show do
      summary 'Returns an employee\'s details'
      param :path, :id, :integer, :required, "User ID"
    end
    def show
      render json: @employee, status: :ok
    end

    # POST /employees
    swagger_api :create do
      summary 'Creates an employee'
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end

    def create
      @employee = Employee.new(employee_params)

      if @employee.save
        render json: @employee, status: :created
      else
        render json: @employee.errors, status: :unprocessable_entity
      end
    end

    # PATCH/PUT /employees/1
    swagger_api :update do
      summary 'Updates an employee\'s details'
      param :path, :id, :integer, :required, "User ID"
      param :body, :body, :string, :required, "Request body"
      param :header, :Authorization, :string, :required, "Token"
    end
    def update
      if @employee.update(employee_params)
        render json: @employee, status: :ok
      else
        render json: @employee.errors, status: :unprocessable_entity
      end
    end

    # DELETE /employees/1
    swagger_api :destroy do
      summary 'Deletes an employee'
      param :path, :id, :integer, :required, "Employee ID"
      param :header, :Authorization, :string, :required, "Token"
    end

    def destroy
      @employee.destroy
      render json: { "Status":"Deleted" }, status: :ok
    end

    private

    def set_employee
      @employee = Employee.find(params[:id])
    end

    def employee_params
      params.permit(:user_id, :department, :manager_id, :position_id)
    end
  end
end

