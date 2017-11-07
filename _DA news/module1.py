# Import the helper gateway class
from africastalking.AfricasTalkingGateway import (AfricasTalkingGateway, AfricasTalkingGatewayException)
# Specify your login credentials
username = "sandbox"
apikey   = "118f15717e3f65435c25e5afdf60b67682e2aafabb2b4bcf89f161c236225340"

# Please ensure you include the country code (+254 for Kenya in this case)
to      = "+254702478983"

message = "I'm a lumberjack and it's ok, I sleep all night and I work all day"

# Create a new instance of our awesome gateway class

gateway = AfricasTalkingGateway(username, apikey, environment='sandbox')

try:
    # Thats it, hit send and we'll take care of the rest.
    
    results = gateway.sendMessage(to, message)

    for recipient in results:
        # status is either "Success" or "error message"
        print 'number=%s;status=%s;messageId=%s;cost=%s' %(recipient['number'],
                                                        recipient['status'],
                                                        recipient['messageId'],
                                                        recipient['cost'])
except AfricasTalkingGatewayException, e:
    print 'Encountered an error while sending: %s' % str(e)