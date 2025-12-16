import boto3


# Create EC2 resource and client
ec2 = boto3.resource('ec2')
ec2_client = boto3.client('ec2')

# Start an on-demand nano EC2 instance
def start_nano_instance(image_id=None, key_name=None, security_group_id=None, root_volume_size=10, region='ap-southeast-2'):
  
    try:
        # Prepare instance parameters
        params = {
            'ImageId': image_id or 'ami-0b3c832b6b7289e44',  # Amazon Linux 2 in ap-southeast-2
            'MinCount': 1,
            'MaxCount': 1,
            'InstanceType': 't2.nano',  # Nano instance type
            'BlockDeviceMappings': [
                {
                    'DeviceName': '/dev/xvda',  # Root device for Amazon Linux
                    'Ebs': {
                        'VolumeSize': root_volume_size,  # Size in GB
                        'VolumeType': 'gp2',  # General purpose SSD
                        'DeleteOnTermination': True
                    }
                }
            ]
        }
        
        if key_name:
            params['KeyName'] = key_name
        
        if security_group_id:
            params['SecurityGroupIds'] = [security_group_id]
        
        
        instances = ec2.create_instances(**params)
        instance = instances[0]
        
        print(f"Starting EC2 instance...")
        print(f"Instance ID: {instance.id}")
        print(f"Instance Type: {instance.instance_type}")
        print(f"State: {instance.state['Name']}")
        
       
        instance.wait_until_running()
        instance.reload()
        
        print(f"\nInstance is now running!")
        print(f"Public IP: {instance.public_ip_address}")
        print(f"Private IP: {instance.private_ip_address}")
        
        return instance
    
    except Exception as e:
        print(f"Error starting instance: {str(e)}")
        return None

# Example usage
if __name__ == "__main__":
  
    IMAGE_ID = 'ami-0b3c832b6b7289e44'  # Amazon Linux 2 in ap-southeast-2
    KEY_NAME = 'huynq-intern-key'      # Your EC2 key pair
       
    
    instance = start_nano_instance(
        image_id=IMAGE_ID,
        key_name=KEY_NAME,
        
    )
