from aws_cdk import (
    core,
    aws_ec2 as ec2,
    aws_ecr as ecr
)


class CommonStack(core.Stack):
    def __init__(self, scope: core.Construct, id: str, props, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # create an umccrise ECR repo to deploy the created images to (defined in build spec)
        ecr_repo = ecr.Repository(
            self,
            id="UmccriseEcrRepo",
            repository_name=props['umccrise_ecr_repo'],
            removal_policy=core.RemovalPolicy.RETAIN
        )
        # We assign the repo's arn to a local variable for the Object.
        self._ecr_name = ecr_repo.repository_name
        self._ecr_arn = ecr_repo.repository_arn

        # Common VPC setup
        # TODO: roll out across all AZs? (Will require more subnets, NATs, ENIs, etc...)
        vpc = ec2.Vpc(
            self,
            'UmccrVpc',
            cidr="10.2.0.0/16",
            max_azs=1
        )
        self._vpc = vpc


    # Using the property decorator to expose properties of the common setup
    @property
    def ecr_name(self):
        return self._ecr_name

    @property
    def ecr_arn(self):
        return self._ecr_arn

    @property
    def vpc(self):
        return self._vpc
