<script setup>

import {onMounted, ref} from "vue";

const props = defineProps({
  employee: Object
})

const $emit = defineEmits(['delete'])

onMounted(() => {
  fullName.value = props.employee['full_name']
  phoneNumber.value = props.employee['phone_number']
  emailAddress.value = props.employee['email_address']
  salary.value = props.employee['salary']
})

const editMode = ref(false)

// employees fields
const fullName = ref("")
const phoneNumber = ref("")
const emailAddress = ref("")
const salary = ref("")

async function switchEditMode() {
  props.employee['full_name'] = fullName.value
  props.employee['phone_number'] = phoneNumber.value
  props.employee['email_address'] = emailAddress.value
  props.employee['salary'] = salary.value
  editMode.value = !editMode.value
}

async function validateInput() {
  return !(fullName.value.length === 0 ||
      (isNaN(parseFloat(salary.value))));
}

async function editEmployee() {
  if (!await validateInput()) {
    alert("Fields: full_name and salary must be filled. Salary must be a number.")
    return
  }

  fullName.value = props.employee['full_name']
  phoneNumber.value = props.employee['phone_number']
  emailAddress.value = props.employee['email_address']
  salary.value = props.employee['salary']

  eel.edit(
      props.employee['employee_id'],
      fullName.value,
      phoneNumber.value,
      emailAddress.value,
      salary.value
  )
  editMode.value = false
}

async function deleteEmployee() {
  eel.delete(props.employee['employee_id'])
  $emit('delete')
}
</script>

<template>
  <!--
  employee['employee_id']
  employee['full_name']
  employee['phone_number']
  employee['email_address']
  employee['salary']
  -->
  <th scope="row">
    {{ employee['employee_id'] }}
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="text" v-model="employee['full_name']">
    <input v-else class="form-control disabled" readonly v-model="fullName">
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="tel" v-model="employee['phone_number']">
    <input v-else class="form-control disabled" readonly v-model="phoneNumber">
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="email" v-model="employee['email_address']">
    <input v-else class="form-control disabled" readonly v-model="emailAddress">
  </th>
  <th>
    <input class="form-control" v-if="editMode" type="text" v-model="employee['salary']">
    <input v-else class="form-control disabled" readonly v-model="salary">
  </th>

  <template v-if="!editMode">
    <th class="btn-primary" @click="switchEditMode">
      <img src="../assets/pen-svgrepo-com.svg" alt="pen icon" width="30" height="30">
    </th>
    <th class="btn-danger" @click="deleteEmployee">
      <img src="../assets/trash-icon.svg" alt="trash icon" width="30" height="30">
    </th>
  </template>

  <template v-else>
    <th class="btn-success" @click="editEmployee">
      <img src="../assets/save-icon-svgrepo-com.svg" alt="save icon" width="30" height="30">
    </th>
    <th class="btn-secondary" @click="switchEditMode">
      <img src="../assets/cancel-svgrepo-com.svg" alt="cancel icon" width="30" height="30">
    </th>
  </template>
</template>

<style scoped>

</style>