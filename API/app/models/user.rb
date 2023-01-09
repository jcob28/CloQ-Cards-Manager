class User < ApplicationRecord
    validates :login, presence: true, uniqueness: true, length: { in: 3..50 }
    validates :first_name, presence: true
    validates :last_name, presence: true
    validates :email, presence: true, uniqueness: true
    validates :account_type, presence: true
    validates :account_no, presence: true, uniqueness: true, length: { is: 28 }
    validates :password, presence: true, length: { minimum: 6 }
    has_secure_password

    has_many :employees
    has_many :managers
end

