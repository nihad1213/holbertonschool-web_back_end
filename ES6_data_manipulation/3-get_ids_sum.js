/* eslint-disable */
export default function getStudentIdsSum(students) {
    if (Object.getPrototypeOf(students) === Array.prototype) {
        const ids = students.map((student) => student.id);
        const reducer = (accumulator, currentValue) => accumulator + currentValue;
        return ids.reduce(reducer, 0);
    }

    return 0;
}
