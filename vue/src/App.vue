<script setup>
import {onMounted, ref} from 'vue'
import EmployeeBlockComponent from "./components/EmployeeBlockComponent.vue";

const employees = ref([])
const loading = ref(false)
const checked = ref([])
const creationMode = ref(false)

const fullName = ref("")
const phoneNumber = ref("")
const emailAddress = ref("")
const salary = ref("")

async function getEmployees() {
  loading.value = true
  employees.value = await eel.get()()
  loading.value = false
}

async function validateInput() {
  return !(fullName.value.length === 0 ||
      (isNaN(parseFloat(salary.value))));
}

/**
 * full_name: str
 * phone_number: str = None
 * email_address: str = None
 * salary: float = None
 */
async function createEmployee() {
  loading.value = true
  if (!await validateInput()) {
    alert("Fields: full_name and salary must be filled. Salary must be a number.")
    loading.value = false
    return
  }
  await eel.create(
      fullName.value,
      phoneNumber.value,
      emailAddress.value,
      salary.value
  )()
  emptyFields()
  await getEmployees()
  loading.value = false
}

async function emptyFields() {
  fullName.value = ""
  phoneNumber.value = ""
  emailAddress.value = ""
  salary.value = ""
}

async function deleteSelected() {
  loading.value = true
  await eel.delete_many(checked.value)()
  await getEmployees()
  loading.value = false
}

onMounted(() => {
  getEmployees()
})
</script>

<template>
  <table class="table table-bordered table-hover">
    <thead>
    <tr>
      <th colspan="4" class="btn-success" @click="creationMode = true; emptyFields()">
        <img src="./assets/plus-svgrepo-com.svg" alt="plus icon" width="30" height="30">
      </th>
      <th colspan="4" class="btn-danger" @click="deleteSelected">
        Delete selected
      </th>
    </tr>
    <!--  creation mode  -->
    <tr v-if="creationMode">
      <th scope="col">
      </th>
      <th scope="col">
      </th>
      <th scope="col">
        <input type="text" class="form-control" v-model="fullName" placeholder="Full Name" required>
      </th>
      <th scope="col">
        <input type="tel" class="form-control" v-model="phoneNumber" placeholder="Phone Number">
      </th>
      <th scope="col">
        <input type="email" class="form-control" v-model="emailAddress" placeholder="Email Address">
      </th>
      <th scope="col">
        <input type="text" class="form-control" v-model="salary" placeholder="Salary">
      </th>
      <th class="btn-success" @click="createEmployee">
        <img src="./assets/save-icon-svgrepo-com.svg" alt="save icon" width="30" height="30">
      </th>
      <th class="btn-danger" @click="creationMode = false; emptyFields()">
        <img src="./assets/cancel-svgrepo-com.svg" alt="cancel icon" width="30" height="30">
      </th>
    </tr>
    <!--  header  -->
    <tr>
      <th scope="col">
      </th>
      <th scope="col">
        #
      </th>
      <th scope="col">
        Full Name
      </th>
      <th scope="col">
        Phone Number
      </th>
      <th scope="col">
        Email Address
      </th>
      <th scope="col">
        Salary
      </th>
      <th scope="col" colspan="2">
        Actions
      </th>
    </tr>
    </thead>
    <tbody>
    <tr v-if="!loading" v-for="employee in employees">
      <th>
        <input type="checkbox" v-model="checked" :value="employee['employee_id']">
      </th>
      <employee-block-component @delete="getEmployees" :employee="employee"/>
    </tr>
    <tr v-else>
      <th colspan="8">
        <h1>Loading</h1>
      </th>
    </tr>
    </tbody>
  </table>
</template>

<style scoped>

</style>
