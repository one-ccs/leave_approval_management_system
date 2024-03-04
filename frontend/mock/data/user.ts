import { faker } from "@faker-js/faker/locale/zh_CN";
import role from './role';
import major from './major';

const random = () => {
    return {
        name: faker.person.fullName(),
        role: role(),
        major: major(),
    };
};

export default random;
