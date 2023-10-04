<script setup>
import {onMounted, ref} from 'vue'
import EmployeeBlockComponent from "./components/EmployeeBlockComponent.vue";

const employees = ref([])
const loading = ref(false)
const checked = ref([])
const creationMode = ref(false)

async function getEmployees() {
  loading.value = true
  employees.value = await eel.get()()
  loading.value = false
}

/**
 * full_name: str
 * phone_number: str = None
 * email_address: str = None
 * salary: float = None
 */
async function createEmployee() {
  loading.value = true
  await eel.create(
      this.$refs.fullName.value,
      this.$refs.phoneNumber.value,
      this.$refs.emailAddress.value,
      this.$refs.salary.value
  )()
  loading.value = false
}

async function checkAll() {
  checked.value = []
}

async function deleteSelected() {
  loading.value = true
  await eel.delete(checked.value)()
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
      <th colspan="4" class="btn-success" @click="creationMode = true">
        Add new
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
        <input type="text" placeholder="Full Name" required :ref="'fullName'">
      </th>
      <th scope="col">
        <input type="tel" placeholder="Phone Number" :ref="'phoneNumber'">
      </th>
      <th scope="col">
        <input type="email" placeholder="Email Address" :ref="'emailAddress'">
      </th>
      <th scope="col">
        <input type="text" placeholder="Salary" :ref="'salary'">
      </th>
      <th class="btn-success" @click="createEmployee">
        Create
      </th>
      <th class="btn-danger" @click="creationMode = false">
        Cancel
      </th>
    </tr>
    <!--  header  -->
    <tr>
      <th scope="col">
        <input type="checkbox">
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
        <input type="checkbox" :ref="employee['employee_id']">
      </th>
      <employee-block-component :employee="employee"/>
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
