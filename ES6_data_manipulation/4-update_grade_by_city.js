/* eslint-disable */
export default function updateStudentGradeByCity(arrOfStudentObjs, city, newGrades) {
  if (Array.isArray(arrOfStudentObjs) && typeof city === 'string' && Array.isArray(newGrades)) {
    // Filter students based on city
    const filteredStudents = arrOfStudentObjs.filter(student => student.location === city);

    // Map through filtered students and update grades
    const updatedStudents = filteredStudents.map(student => {
      const gradeObj = newGrades.find(grade => grade.studentId === student.id);
      if (gradeObj) {
        return { ...student, grade: gradeObj.grade };
      } else {
        return { ...student, grade: 'N/A' };
      }
    });

    return updatedStudents;
  }
  return [];
}
