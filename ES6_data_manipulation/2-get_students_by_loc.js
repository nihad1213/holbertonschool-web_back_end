/* eslint-disable */
export default function getStudentsByLocation() {
    if (Object.getPrototypeOf(students) === Array.prototype) {
        return students.filter((nihad) => nihad.location === city);
    }

    return []
}