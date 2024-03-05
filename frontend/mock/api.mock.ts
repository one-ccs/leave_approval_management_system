import { defineMock } from 'vite-plugin-mock-dev-server'
import user from './data/user';

export default defineMock([
    {
        url: '/api/user/login',
        body: () => ({
          code: 200,
          message: '登录成功',
          data: user(),
        }),
    },
    {
        url: '/api/user/logout',
        body: () => ({
          code: 200,
          message: '登出成功',
          data: true,
        }),
    },
])
