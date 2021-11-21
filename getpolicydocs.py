import boto3

iam = boto3.resource('iam')

def get_policy_body(arn,version_id=None):
    if version_id:
        version = iam.PolicyVersion(arn,version_id)
    else:
        policy = iam.Policy(arn)
        version = policy.default_version
    return version.document

policy_arn = "arn:aws:iam::aws:policy/AdministratorAccess-AWSElasticBeanstalk"
body = get_policy_body(policy_arn)

print("Policy body: %s" % body)