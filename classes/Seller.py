"""This module defins the Seller class."""
    @property
    def services_offered(self, services_offered: list) -> list:
        """The services offered by the seller.
        
        Arguments:
            services_offered (list): list of services offered by the seller.
            
        Returns: 
            list: list of names of services offered by the seller."""
            
        return [service.name for service in services_offered]