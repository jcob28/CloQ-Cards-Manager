include Swagger::Docs::ImpotentMethods

class Swagger::Docs::Config
  def self.base_api_controller
    ActionController::API
  end
end