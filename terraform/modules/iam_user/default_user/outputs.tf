# module outputs
# i.e. the attributes of the module component
output "username" {
  value = "${var.username}"
}

output "arn" {
  value = "${aws_iam_user.iam_user.arn}"
}

output "access_key" {
  value = "${aws_iam_access_key.iam_access_key.id}"
}

# NOTE: NOT SAFE!! use secure user instead
output "secret_access_key" {
  value = "${aws_iam_access_key.iam_access_key.secret}"
}
