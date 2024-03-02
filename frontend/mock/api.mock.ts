import { defineMock } from 'vite-plugin-mock-dev-server'

export default defineMock([
    {
        url: '/api/user/login',
        body: {
          code: 200,
          message: '登录成功',
          data: {
            username: 'ua',
            roles: ['学生'],
          },
        },
    },
])
