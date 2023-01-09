json.extract! employee, :id, :employee_id, :user_id, :department, :manager_id, :position_id, :created_at, :updated_at
json.url employee_url(employee, format: :json)
