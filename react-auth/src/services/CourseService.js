import axios from 'axios';
export function addCourse(course) {
    console.log(course.date.value);
    return axios.post('http://127.0.0.1:8000/courses/', {
        
        depart:course.depart.value,
        destination:course.destination.value,
        distance:course.distance.value,
        montant:course.montant.value,
        description: course.description.value,
        user:localStorage.getItem("id"),
        date:course.date.value
    })
        .then(response => response.data)
}