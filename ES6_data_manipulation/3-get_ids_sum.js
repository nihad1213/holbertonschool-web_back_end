/* eslint-disable */
export default function getStudentIdsSum(students) {
    if (Object.getPrototypeOf(students) === Array.prototype) {
        const ids = stduents.map((ids) => ids.id);
        const reducer = (accumlator, currentValue) => accumlator + currentValue;
        return ids.reduce(reducer);
    }

    return [];
}