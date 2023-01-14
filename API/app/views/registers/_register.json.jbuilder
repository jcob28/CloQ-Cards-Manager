json.extract! register, :id, :register_id, :employee_id, :gate_id, :date_in, :time_in, :date_out, :time_out, :created_at, :updated_at
json.url register_url(register, format: :json)
