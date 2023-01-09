class Employee < ApplicationRecord
  belongs_to :user
  belongs_to :manager
  belongs_to :position
  has_many :registers
  has_many :vacations
end
