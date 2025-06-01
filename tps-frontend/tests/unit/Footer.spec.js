import { mount } from '@vue/test-utils';
import Footer from '@/components/layout/Footer.vue'; // Adjust path if needed, @ usually points to src

// Mocking new Date().getFullYear() can be done if specific year testing is needed
// For example, by using vi.spyOn(Date.prototype, 'getFullYear').mockReturnValue(2024); in Vitest/Jest

describe('Footer.vue', () => {
  it('renders copyright text including the current year', () => {
    const wrapper = mount(Footer);
    const currentYear = new Date().getFullYear();

    // Check if the component contains the copyright symbol and part of the text
    expect(wrapper.text()).toContain('©');
    expect(wrapper.text()).toContain(String(currentYear)); // Check for current year
    expect(wrapper.text()).toContain('Tacoma Parking Services');
  });

  it('contains links for Privacy Policy and Terms of Service', () => {
    const wrapper = mount(Footer);
    const links = wrapper.findAll('a'); // Find all anchor tags

    // Check if there are at least two links
    expect(links.length).toBeGreaterThanOrEqual(2);

    const privacyPolicyLink = links.find(link => link.text().includes('Privacy Policy'));
    const termsOfServiceLink = links.find(link => link.text().includes('Terms of Service'));

    expect(privacyPolicyLink).toBeTruthy(); // Check if the link element exists
    expect(termsOfServiceLink).toBeTruthy(); // Check if the link element exists

    // Optionally check href attributes if they are static placeholders
    // These are simple <a> tags in the current Footer.vue implementation
    if (privacyPolicyLink) { // Ensure link exists before checking attribute
        expect(privacyPolicyLink.attributes('href')).toBe('#');
    }
    if (termsOfServiceLink) { // Ensure link exists before checking attribute
        expect(termsOfServiceLink.attributes('href')).toBe('#');
    }
  });
});
