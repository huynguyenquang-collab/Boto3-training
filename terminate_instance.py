import boto3

#terminate created instance from start_instance.py
def terminate_instance(instance_id, region='ap-southeast-2'):
    try:
        # Create EC2 resource
        ec2 = boto3.resource('ec2', region_name=region)
        
        # Get the instance
        instance = ec2.Instance(instance_id)
        
        print(f"Terminating EC2 instance {instance_id}...")
        
        # Terminate the instance
        response = instance.terminate()
        
        print(f"Termination initiated. Current state: {response['TerminatingInstances'][0]['CurrentState']['Name']}")
        
        # Wait until the instance is terminated
        instance.wait_until_terminated()
        
        print(f"Instance {instance_id} has been terminated.")
        
    except Exception as e:
        print(f"Error terminating instance: {str(e)}")
   
  


if __name__ == "__main__":
    test_instance_id = "i-08c2c36ebc2b65c6d"  # Replace with your instance ID
    terminate_instance(test_instance_id)
  
