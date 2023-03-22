source 'https://rubygems.org'

ruby '3.0.2'

# 添加依赖项
gem 'nokogiri', '1.12.5'

# 添加依赖项并指定版本范围
gem 'rails', '>= 6.1.0', '< 7.0'

# 添加开发和测试环境的依赖项
group :development, :test do
  gem 'rspec-rails', '~> 5.0.0'
end

# 添加只在特定环境的依赖项
group :production do
  gem 'unicorn', '6.0.0'
end

# 添加依赖项并指定来源
gem 'sinatra', '2.1.0', source: 'https://rubygems.org'

# 添加依赖项并指定 Git 仓库
gem 'rack', git: 'https://github.com/rack/rack.git', tag: '2.2.3'

# 添加依赖项并指定本地路径
# gem 'my_gem', path: 'path/to/my_gem'

# 使用多个来源
source 'https://rubygems.org' do
  gem 'puma', '5.5.2'
end

source 'https://gems.example.com' do
  # 假设存在一个名为 'my_private_gem' 的私有 gem
  # gem 'my_private_gem', '1.0.0'
end
