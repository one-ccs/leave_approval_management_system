import { faker } from "@faker-js/faker/locale/zh_CN";

const random = () => {
    const grade = faker.number.int({min: 10, max: 24});
    const major = faker.string.fromCharacters(['计算机科学与技术', '人工智能大数据', '软件工程']);
    const _class = faker.number.int({min: 1, max: 18});

    return `${grade}${major}${_class}班`;
};

export default random;
