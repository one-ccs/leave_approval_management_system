import { faker } from "@faker-js/faker/locale/zh_CN";

const random = () => {
    return faker.string.fromCharacters(['学生', '辅导员', '管理员']);
};

export default random;
