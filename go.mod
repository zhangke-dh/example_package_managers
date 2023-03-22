module example.com/myproject

go 1.17

require (
    github.com/gin-gonic/gin v1.7.7                       // 1. 基本语法
    golang.org/x/net v0.0.0-20211021110250-2f3e3b1d35bb   // 2. 使用指定的 commit hash的伪版本
    
    github.com/gorilla/mux branch_name                    // 3. 使用分支名称
    github.com/stretchr/testify v1.6.1-custom             // 4. 使用标签名称
)

replace (
    github.com/gin-gonic/gin => github.com/myfork/gin v1.7.7-custom // 5. 使用替代模块
    golang.org/x/net => ../x-net                                    // 6. 使用本地文件系统路径
)

exclude (
    github.com/stretchr/testify v1.6.0 // 7. 指定的依赖项不适用于某些版本
)
