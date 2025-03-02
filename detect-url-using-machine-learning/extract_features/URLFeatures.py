from .domain import domain
from .dom import dom
from .addressBar import addressBar

class URLFeatures:
    def __init__(self, url):
        self.url = url
        self.addressbar = addressBar(url)
        self.domain = domain(url)
        self.dom = dom(url)
        
    def __getaddressbar__(self, feature_name):
        return self.addressbar.get(feature_name, None)
    
    def __getdomain__(self, feature_name):
        return self.domain.get(feature_name, None)
    
    def __getdom__(self, feature_name):
        return self.dom.get(feature_name, None)
    
    # get all
    def get_all_features(self):
        all_features = {}

        # Kết hợp tất cả các features từ addressbar, domain, và dom
        addressbar_features = self.addressbar
        domain_features = self.domain
        dom_features = self.dom

        # Thêm các feature từ addressbar
        all_features.update(addressbar_features)

        # Thêm các feature từ domain (nếu có)
        if domain_features:
            all_features.update(domain_features)

        # Thêm các feature từ dom (nếu có)
        if dom_features:
            all_features.update(dom_features)

        return all_features
if __name__ == "__main__":
    url = "https://www.kaggle.com/"  # test
    result = URLFeatures(url)
    # In tất cả các features
    for feature_name, value in result.get_all_features().items():
        print(f"{feature_name}: {value}")